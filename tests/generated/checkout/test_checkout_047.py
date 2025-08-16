import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-2761", "title": "Checkout scenario 2761", "data": {"sku": "SKU2761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2761@example.com", "threshold": 610}},
    {"id": "CHECKOUT-2762", "title": "Checkout scenario 2762", "data": {"sku": "SKU2762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2762@example.com", "threshold": 620}},
    {"id": "CHECKOUT-2763", "title": "Checkout scenario 2763", "data": {"sku": "SKU2763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2763@example.com", "threshold": 630}},
    {"id": "CHECKOUT-2764", "title": "Checkout scenario 2764", "data": {"sku": "SKU2764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2764@example.com", "threshold": 640}},
    {"id": "CHECKOUT-2765", "title": "Checkout scenario 2765", "data": {"sku": "SKU2765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2765@example.com", "threshold": 650}},
    {"id": "CHECKOUT-2766", "title": "Checkout scenario 2766", "data": {"sku": "SKU2766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2766@example.com", "threshold": 660}},
    {"id": "CHECKOUT-2767", "title": "Checkout scenario 2767", "data": {"sku": "SKU2767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2767@example.com", "threshold": 670}},
    {"id": "CHECKOUT-2768", "title": "Checkout scenario 2768", "data": {"sku": "SKU2768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2768@example.com", "threshold": 680}},
    {"id": "CHECKOUT-2769", "title": "Checkout scenario 2769", "data": {"sku": "SKU2769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2769@example.com", "threshold": 690}},
    {"id": "CHECKOUT-2770", "title": "Checkout scenario 2770", "data": {"sku": "SKU2770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2770@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
