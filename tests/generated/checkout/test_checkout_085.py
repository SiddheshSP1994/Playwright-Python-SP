import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5041", "title": "Checkout scenario 5041", "data": {"sku": "SKU5041", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5041@example.com", "threshold": 410}},
    {"id": "CHECKOUT-5042", "title": "Checkout scenario 5042", "data": {"sku": "SKU5042", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5042@example.com", "threshold": 420}},
    {"id": "CHECKOUT-5043", "title": "Checkout scenario 5043", "data": {"sku": "SKU5043", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5043@example.com", "threshold": 430}},
    {"id": "CHECKOUT-5044", "title": "Checkout scenario 5044", "data": {"sku": "SKU5044", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5044@example.com", "threshold": 440}},
    {"id": "CHECKOUT-5045", "title": "Checkout scenario 5045", "data": {"sku": "SKU5045", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5045@example.com", "threshold": 450}},
    {"id": "CHECKOUT-5046", "title": "Checkout scenario 5046", "data": {"sku": "SKU5046", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5046@example.com", "threshold": 460}},
    {"id": "CHECKOUT-5047", "title": "Checkout scenario 5047", "data": {"sku": "SKU5047", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5047@example.com", "threshold": 470}},
    {"id": "CHECKOUT-5048", "title": "Checkout scenario 5048", "data": {"sku": "SKU5048", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5048@example.com", "threshold": 480}},
    {"id": "CHECKOUT-5049", "title": "Checkout scenario 5049", "data": {"sku": "SKU5049", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5049@example.com", "threshold": 490}},
    {"id": "CHECKOUT-5050", "title": "Checkout scenario 5050", "data": {"sku": "SKU5050", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5050@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
