import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5761", "title": "Checkout scenario 5761", "data": {"sku": "SKU5761", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5761@example.com", "threshold": 610}},
    {"id": "CHECKOUT-5762", "title": "Checkout scenario 5762", "data": {"sku": "SKU5762", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5762@example.com", "threshold": 620}},
    {"id": "CHECKOUT-5763", "title": "Checkout scenario 5763", "data": {"sku": "SKU5763", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5763@example.com", "threshold": 630}},
    {"id": "CHECKOUT-5764", "title": "Checkout scenario 5764", "data": {"sku": "SKU5764", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5764@example.com", "threshold": 640}},
    {"id": "CHECKOUT-5765", "title": "Checkout scenario 5765", "data": {"sku": "SKU5765", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5765@example.com", "threshold": 650}},
    {"id": "CHECKOUT-5766", "title": "Checkout scenario 5766", "data": {"sku": "SKU5766", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5766@example.com", "threshold": 660}},
    {"id": "CHECKOUT-5767", "title": "Checkout scenario 5767", "data": {"sku": "SKU5767", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5767@example.com", "threshold": 670}},
    {"id": "CHECKOUT-5768", "title": "Checkout scenario 5768", "data": {"sku": "SKU5768", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5768@example.com", "threshold": 680}},
    {"id": "CHECKOUT-5769", "title": "Checkout scenario 5769", "data": {"sku": "SKU5769", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5769@example.com", "threshold": 690}},
    {"id": "CHECKOUT-5770", "title": "Checkout scenario 5770", "data": {"sku": "SKU5770", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5770@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
