import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-6841", "title": "Checkout scenario 6841", "data": {"sku": "SKU6841", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6841@example.com", "threshold": 410}},
    {"id": "CHECKOUT-6842", "title": "Checkout scenario 6842", "data": {"sku": "SKU6842", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6842@example.com", "threshold": 420}},
    {"id": "CHECKOUT-6843", "title": "Checkout scenario 6843", "data": {"sku": "SKU6843", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6843@example.com", "threshold": 430}},
    {"id": "CHECKOUT-6844", "title": "Checkout scenario 6844", "data": {"sku": "SKU6844", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6844@example.com", "threshold": 440}},
    {"id": "CHECKOUT-6845", "title": "Checkout scenario 6845", "data": {"sku": "SKU6845", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6845@example.com", "threshold": 450}},
    {"id": "CHECKOUT-6846", "title": "Checkout scenario 6846", "data": {"sku": "SKU6846", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6846@example.com", "threshold": 460}},
    {"id": "CHECKOUT-6847", "title": "Checkout scenario 6847", "data": {"sku": "SKU6847", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6847@example.com", "threshold": 470}},
    {"id": "CHECKOUT-6848", "title": "Checkout scenario 6848", "data": {"sku": "SKU6848", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6848@example.com", "threshold": 480}},
    {"id": "CHECKOUT-6849", "title": "Checkout scenario 6849", "data": {"sku": "SKU6849", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6849@example.com", "threshold": 490}},
    {"id": "CHECKOUT-6850", "title": "Checkout scenario 6850", "data": {"sku": "SKU6850", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6850@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
