import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-9601", "title": "Checkout scenario 9601", "data": {"sku": "SKU9601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9601@example.com", "threshold": 10}},
    {"id": "CHECKOUT-9602", "title": "Checkout scenario 9602", "data": {"sku": "SKU9602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9602@example.com", "threshold": 20}},
    {"id": "CHECKOUT-9603", "title": "Checkout scenario 9603", "data": {"sku": "SKU9603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9603@example.com", "threshold": 30}},
    {"id": "CHECKOUT-9604", "title": "Checkout scenario 9604", "data": {"sku": "SKU9604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9604@example.com", "threshold": 40}},
    {"id": "CHECKOUT-9605", "title": "Checkout scenario 9605", "data": {"sku": "SKU9605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9605@example.com", "threshold": 50}},
    {"id": "CHECKOUT-9606", "title": "Checkout scenario 9606", "data": {"sku": "SKU9606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9606@example.com", "threshold": 60}},
    {"id": "CHECKOUT-9607", "title": "Checkout scenario 9607", "data": {"sku": "SKU9607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9607@example.com", "threshold": 70}},
    {"id": "CHECKOUT-9608", "title": "Checkout scenario 9608", "data": {"sku": "SKU9608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9608@example.com", "threshold": 80}},
    {"id": "CHECKOUT-9609", "title": "Checkout scenario 9609", "data": {"sku": "SKU9609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9609@example.com", "threshold": 90}},
    {"id": "CHECKOUT-9610", "title": "Checkout scenario 9610", "data": {"sku": "SKU9610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9610@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
