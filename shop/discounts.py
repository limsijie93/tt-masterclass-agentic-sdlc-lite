"""Discount engine. Pluggable so marketing can run any kind of deal."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime


class DiscountRule(ABC):
    @abstractmethod
    def discount(self, subtotal: int) -> int:
        """Amount in cents to take off the subtotal."""


@dataclass
class PercentageOff(DiscountRule):
    percent: int

    def discount(self, subtotal: int) -> int:
        return subtotal * self.percent // 100


@dataclass
class FixedAmountOff(DiscountRule):
    amount_cents: int

    def discount(self, subtotal: int) -> int:
        return min(self.amount_cents, subtotal)


RULE_TYPES: dict[str, type[DiscountRule]] = {}


def register_rule(name: str, rule_type: type[DiscountRule]) -> None:
    RULE_TYPES[name] = rule_type


register_rule("percentage", PercentageOff)
register_rule("fixed", FixedAmountOff)


@dataclass
class PromoCode:
    code: str
    rules: list[DiscountRule] = field(default_factory=list)
    expires_at: datetime | None = None
    stackable: bool = False

    def is_active(self, now: datetime) -> bool:
        return self.expires_at is None or now < self.expires_at


def build_promo(code: str, config: dict) -> PromoCode:
    rules = [RULE_TYPES[r["type"]](**r["params"]) for r in config["rules"]]
    return PromoCode(code, rules, config.get("expires_at"), config.get("stackable", False))
