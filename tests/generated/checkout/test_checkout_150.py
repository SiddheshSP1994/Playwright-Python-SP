import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-8941", "title": "Checkout scenario 8941", "data": {"sku": "SKU8941", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8941@example.com", "threshold": 410}},
    {"id": "CHECKOUT-8942", "title": "Checkout scenario 8942", "data": {"sku": "SKU8942", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8942@example.com", "threshold": 420}},
    {"id": "CHECKOUT-8943", "title": "Checkout scenario 8943", "data": {"sku": "SKU8943", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8943@example.com", "threshold": 430}},
    {"id": "CHECKOUT-8944", "title": "Checkout scenario 8944", "data": {"sku": "SKU8944", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8944@example.com", "threshold": 440}},
    {"id": "CHECKOUT-8945", "title": "Checkout scenario 8945", "data": {"sku": "SKU8945", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8945@example.com", "threshold": 450}},
    {"id": "CHECKOUT-8946", "title": "Checkout scenario 8946", "data": {"sku": "SKU8946", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8946@example.com", "threshold": 460}},
    {"id": "CHECKOUT-8947", "title": "Checkout scenario 8947", "data": {"sku": "SKU8947", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8947@example.com", "threshold": 470}},
    {"id": "CHECKOUT-8948", "title": "Checkout scenario 8948", "data": {"sku": "SKU8948", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8948@example.com", "threshold": 480}},
    {"id": "CHECKOUT-8949", "title": "Checkout scenario 8949", "data": {"sku": "SKU8949", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8949@example.com", "threshold": 490}},
    {"id": "CHECKOUT-8950", "title": "Checkout scenario 8950", "data": {"sku": "SKU8950", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8950@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
