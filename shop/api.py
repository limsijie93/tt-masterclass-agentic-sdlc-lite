"""Entry point. Translates a request into a service call. Never touches repo directly."""

import json

from shop import repo, service


def checkout(payload: dict) -> dict:
    try:
        code = payload.get("promo_code")
        total = service.order_total(payload["items"], code)
        response = {"status": 200, "total_cents": total}
        if code:
            response["discount_percent"] = repo.get_promo_percent(code)
            response["receipt_line"] = service.receipt_line(code, response["discount_percent"])
        return response
    except KeyError:
        return {"status": 400, "error": "missing field: items"}
    except ValueError as e:
        return {"status": 400, "error": str(e)}
