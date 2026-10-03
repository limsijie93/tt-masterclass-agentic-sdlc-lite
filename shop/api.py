"""Entry point. Translates a request into a service call. Never touches repo directly."""

import json

from shop import repo, service


def checkout(payload: dict) -> dict:
    for code in payload.get("promo_codes", []):
        if repo.get_promo_config(code) is None:
            return {"status": 400, "error": f"unknown promo code: {code}"}
    try:
        total = service.order_total(payload["items"], payload.get("promo_codes"))
        return {"status": 200, "total_cents": total}
    except KeyError:
        return {"status": 400, "error": "missing field: items"}
    except ValueError as e:
        return {"status": 400, "error": str(e)}
