import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0121", "title": "Checkout scenario 121", "data": {"sku": "SKU121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user121@example.com", "threshold": 210}},
    {"id": "CHECKOUT-0122", "title": "Checkout scenario 122", "data": {"sku": "SKU122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user122@example.com", "threshold": 220}},
    {"id": "CHECKOUT-0123", "title": "Checkout scenario 123", "data": {"sku": "SKU123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user123@example.com", "threshold": 230}},
    {"id": "CHECKOUT-0124", "title": "Checkout scenario 124", "data": {"sku": "SKU124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user124@example.com", "threshold": 240}},
    {"id": "CHECKOUT-0125", "title": "Checkout scenario 125", "data": {"sku": "SKU125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user125@example.com", "threshold": 250}},
    {"id": "CHECKOUT-0126", "title": "Checkout scenario 126", "data": {"sku": "SKU126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user126@example.com", "threshold": 260}},
    {"id": "CHECKOUT-0127", "title": "Checkout scenario 127", "data": {"sku": "SKU127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user127@example.com", "threshold": 270}},
    {"id": "CHECKOUT-0128", "title": "Checkout scenario 128", "data": {"sku": "SKU128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user128@example.com", "threshold": 280}},
    {"id": "CHECKOUT-0129", "title": "Checkout scenario 129", "data": {"sku": "SKU129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user129@example.com", "threshold": 290}},
    {"id": "CHECKOUT-0130", "title": "Checkout scenario 130", "data": {"sku": "SKU130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user130@example.com", "threshold": 300}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
