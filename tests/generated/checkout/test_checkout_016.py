import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0901", "title": "Checkout scenario 901", "data": {"sku": "SKU901", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user901@example.com", "threshold": 10}},
    {"id": "CHECKOUT-0902", "title": "Checkout scenario 902", "data": {"sku": "SKU902", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user902@example.com", "threshold": 20}},
    {"id": "CHECKOUT-0903", "title": "Checkout scenario 903", "data": {"sku": "SKU903", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user903@example.com", "threshold": 30}},
    {"id": "CHECKOUT-0904", "title": "Checkout scenario 904", "data": {"sku": "SKU904", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user904@example.com", "threshold": 40}},
    {"id": "CHECKOUT-0905", "title": "Checkout scenario 905", "data": {"sku": "SKU905", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user905@example.com", "threshold": 50}},
    {"id": "CHECKOUT-0906", "title": "Checkout scenario 906", "data": {"sku": "SKU906", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user906@example.com", "threshold": 60}},
    {"id": "CHECKOUT-0907", "title": "Checkout scenario 907", "data": {"sku": "SKU907", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user907@example.com", "threshold": 70}},
    {"id": "CHECKOUT-0908", "title": "Checkout scenario 908", "data": {"sku": "SKU908", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user908@example.com", "threshold": 80}},
    {"id": "CHECKOUT-0909", "title": "Checkout scenario 909", "data": {"sku": "SKU909", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user909@example.com", "threshold": 90}},
    {"id": "CHECKOUT-0910", "title": "Checkout scenario 910", "data": {"sku": "SKU910", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user910@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
