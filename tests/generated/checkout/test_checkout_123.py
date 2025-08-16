import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-7321", "title": "Checkout scenario 7321", "data": {"sku": "SKU7321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7321@example.com", "threshold": 210}},
    {"id": "CHECKOUT-7322", "title": "Checkout scenario 7322", "data": {"sku": "SKU7322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7322@example.com", "threshold": 220}},
    {"id": "CHECKOUT-7323", "title": "Checkout scenario 7323", "data": {"sku": "SKU7323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7323@example.com", "threshold": 230}},
    {"id": "CHECKOUT-7324", "title": "Checkout scenario 7324", "data": {"sku": "SKU7324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7324@example.com", "threshold": 240}},
    {"id": "CHECKOUT-7325", "title": "Checkout scenario 7325", "data": {"sku": "SKU7325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7325@example.com", "threshold": 250}},
    {"id": "CHECKOUT-7326", "title": "Checkout scenario 7326", "data": {"sku": "SKU7326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7326@example.com", "threshold": 260}},
    {"id": "CHECKOUT-7327", "title": "Checkout scenario 7327", "data": {"sku": "SKU7327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7327@example.com", "threshold": 270}},
    {"id": "CHECKOUT-7328", "title": "Checkout scenario 7328", "data": {"sku": "SKU7328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7328@example.com", "threshold": 280}},
    {"id": "CHECKOUT-7329", "title": "Checkout scenario 7329", "data": {"sku": "SKU7329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7329@example.com", "threshold": 290}},
    {"id": "CHECKOUT-7330", "title": "Checkout scenario 7330", "data": {"sku": "SKU7330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7330@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
