import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-4921", "title": "Checkout scenario 4921", "data": {"sku": "SKU4921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4921@example.com", "threshold": 210}},
    {"id": "CHECKOUT-4922", "title": "Checkout scenario 4922", "data": {"sku": "SKU4922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4922@example.com", "threshold": 220}},
    {"id": "CHECKOUT-4923", "title": "Checkout scenario 4923", "data": {"sku": "SKU4923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4923@example.com", "threshold": 230}},
    {"id": "CHECKOUT-4924", "title": "Checkout scenario 4924", "data": {"sku": "SKU4924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4924@example.com", "threshold": 240}},
    {"id": "CHECKOUT-4925", "title": "Checkout scenario 4925", "data": {"sku": "SKU4925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4925@example.com", "threshold": 250}},
    {"id": "CHECKOUT-4926", "title": "Checkout scenario 4926", "data": {"sku": "SKU4926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4926@example.com", "threshold": 260}},
    {"id": "CHECKOUT-4927", "title": "Checkout scenario 4927", "data": {"sku": "SKU4927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4927@example.com", "threshold": 270}},
    {"id": "CHECKOUT-4928", "title": "Checkout scenario 4928", "data": {"sku": "SKU4928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4928@example.com", "threshold": 280}},
    {"id": "CHECKOUT-4929", "title": "Checkout scenario 4929", "data": {"sku": "SKU4929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4929@example.com", "threshold": 290}},
    {"id": "CHECKOUT-4930", "title": "Checkout scenario 4930", "data": {"sku": "SKU4930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4930@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
