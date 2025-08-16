import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6661", "title": "Checkout scenario 6661", "data": {"sku": "SKU6661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6661@example.com", "threshold": 610}},
    {"id": "CHECKOUT-6662", "title": "Checkout scenario 6662", "data": {"sku": "SKU6662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6662@example.com", "threshold": 620}},
    {"id": "CHECKOUT-6663", "title": "Checkout scenario 6663", "data": {"sku": "SKU6663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6663@example.com", "threshold": 630}},
    {"id": "CHECKOUT-6664", "title": "Checkout scenario 6664", "data": {"sku": "SKU6664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6664@example.com", "threshold": 640}},
    {"id": "CHECKOUT-6665", "title": "Checkout scenario 6665", "data": {"sku": "SKU6665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6665@example.com", "threshold": 650}},
    {"id": "CHECKOUT-6666", "title": "Checkout scenario 6666", "data": {"sku": "SKU6666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6666@example.com", "threshold": 660}},
    {"id": "CHECKOUT-6667", "title": "Checkout scenario 6667", "data": {"sku": "SKU6667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6667@example.com", "threshold": 670}},
    {"id": "CHECKOUT-6668", "title": "Checkout scenario 6668", "data": {"sku": "SKU6668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6668@example.com", "threshold": 680}},
    {"id": "CHECKOUT-6669", "title": "Checkout scenario 6669", "data": {"sku": "SKU6669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6669@example.com", "threshold": 690}},
    {"id": "CHECKOUT-6670", "title": "Checkout scenario 6670", "data": {"sku": "SKU6670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6670@example.com", "threshold": 700}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
