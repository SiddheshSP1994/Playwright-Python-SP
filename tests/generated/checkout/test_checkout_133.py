import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7921", "title": "Checkout scenario 7921", "data": {"sku": "SKU7921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7921@example.com", "threshold": 210}},
    {"id": "CHECKOUT-7922", "title": "Checkout scenario 7922", "data": {"sku": "SKU7922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7922@example.com", "threshold": 220}},
    {"id": "CHECKOUT-7923", "title": "Checkout scenario 7923", "data": {"sku": "SKU7923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7923@example.com", "threshold": 230}},
    {"id": "CHECKOUT-7924", "title": "Checkout scenario 7924", "data": {"sku": "SKU7924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7924@example.com", "threshold": 240}},
    {"id": "CHECKOUT-7925", "title": "Checkout scenario 7925", "data": {"sku": "SKU7925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7925@example.com", "threshold": 250}},
    {"id": "CHECKOUT-7926", "title": "Checkout scenario 7926", "data": {"sku": "SKU7926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7926@example.com", "threshold": 260}},
    {"id": "CHECKOUT-7927", "title": "Checkout scenario 7927", "data": {"sku": "SKU7927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7927@example.com", "threshold": 270}},
    {"id": "CHECKOUT-7928", "title": "Checkout scenario 7928", "data": {"sku": "SKU7928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7928@example.com", "threshold": 280}},
    {"id": "CHECKOUT-7929", "title": "Checkout scenario 7929", "data": {"sku": "SKU7929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7929@example.com", "threshold": 290}},
    {"id": "CHECKOUT-7930", "title": "Checkout scenario 7930", "data": {"sku": "SKU7930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7930@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
