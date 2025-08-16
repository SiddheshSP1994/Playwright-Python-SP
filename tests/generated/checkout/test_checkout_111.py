import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6601", "title": "Checkout scenario 6601", "data": {"sku": "SKU6601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6601@example.com", "threshold": 10}},
    {"id": "CHECKOUT-6602", "title": "Checkout scenario 6602", "data": {"sku": "SKU6602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6602@example.com", "threshold": 20}},
    {"id": "CHECKOUT-6603", "title": "Checkout scenario 6603", "data": {"sku": "SKU6603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6603@example.com", "threshold": 30}},
    {"id": "CHECKOUT-6604", "title": "Checkout scenario 6604", "data": {"sku": "SKU6604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6604@example.com", "threshold": 40}},
    {"id": "CHECKOUT-6605", "title": "Checkout scenario 6605", "data": {"sku": "SKU6605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6605@example.com", "threshold": 50}},
    {"id": "CHECKOUT-6606", "title": "Checkout scenario 6606", "data": {"sku": "SKU6606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6606@example.com", "threshold": 60}},
    {"id": "CHECKOUT-6607", "title": "Checkout scenario 6607", "data": {"sku": "SKU6607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6607@example.com", "threshold": 70}},
    {"id": "CHECKOUT-6608", "title": "Checkout scenario 6608", "data": {"sku": "SKU6608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6608@example.com", "threshold": 80}},
    {"id": "CHECKOUT-6609", "title": "Checkout scenario 6609", "data": {"sku": "SKU6609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6609@example.com", "threshold": 90}},
    {"id": "CHECKOUT-6610", "title": "Checkout scenario 6610", "data": {"sku": "SKU6610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6610@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
