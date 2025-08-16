import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-5941", "title": "Checkout scenario 5941", "data": {"sku": "SKU5941", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5941@example.com", "threshold": 410}},
    {"id": "CHECKOUT-5942", "title": "Checkout scenario 5942", "data": {"sku": "SKU5942", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5942@example.com", "threshold": 420}},
    {"id": "CHECKOUT-5943", "title": "Checkout scenario 5943", "data": {"sku": "SKU5943", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5943@example.com", "threshold": 430}},
    {"id": "CHECKOUT-5944", "title": "Checkout scenario 5944", "data": {"sku": "SKU5944", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5944@example.com", "threshold": 440}},
    {"id": "CHECKOUT-5945", "title": "Checkout scenario 5945", "data": {"sku": "SKU5945", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5945@example.com", "threshold": 450}},
    {"id": "CHECKOUT-5946", "title": "Checkout scenario 5946", "data": {"sku": "SKU5946", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5946@example.com", "threshold": 460}},
    {"id": "CHECKOUT-5947", "title": "Checkout scenario 5947", "data": {"sku": "SKU5947", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5947@example.com", "threshold": 470}},
    {"id": "CHECKOUT-5948", "title": "Checkout scenario 5948", "data": {"sku": "SKU5948", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5948@example.com", "threshold": 480}},
    {"id": "CHECKOUT-5949", "title": "Checkout scenario 5949", "data": {"sku": "SKU5949", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5949@example.com", "threshold": 490}},
    {"id": "CHECKOUT-5950", "title": "Checkout scenario 5950", "data": {"sku": "SKU5950", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5950@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
