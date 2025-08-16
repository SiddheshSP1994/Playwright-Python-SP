import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0841", "title": "Checkout scenario 841", "data": {"sku": "SKU841", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user841@example.com", "threshold": 410}},
    {"id": "CHECKOUT-0842", "title": "Checkout scenario 842", "data": {"sku": "SKU842", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user842@example.com", "threshold": 420}},
    {"id": "CHECKOUT-0843", "title": "Checkout scenario 843", "data": {"sku": "SKU843", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user843@example.com", "threshold": 430}},
    {"id": "CHECKOUT-0844", "title": "Checkout scenario 844", "data": {"sku": "SKU844", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user844@example.com", "threshold": 440}},
    {"id": "CHECKOUT-0845", "title": "Checkout scenario 845", "data": {"sku": "SKU845", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user845@example.com", "threshold": 450}},
    {"id": "CHECKOUT-0846", "title": "Checkout scenario 846", "data": {"sku": "SKU846", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user846@example.com", "threshold": 460}},
    {"id": "CHECKOUT-0847", "title": "Checkout scenario 847", "data": {"sku": "SKU847", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user847@example.com", "threshold": 470}},
    {"id": "CHECKOUT-0848", "title": "Checkout scenario 848", "data": {"sku": "SKU848", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user848@example.com", "threshold": 480}},
    {"id": "CHECKOUT-0849", "title": "Checkout scenario 849", "data": {"sku": "SKU849", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user849@example.com", "threshold": 490}},
    {"id": "CHECKOUT-0850", "title": "Checkout scenario 850", "data": {"sku": "SKU850", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user850@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
