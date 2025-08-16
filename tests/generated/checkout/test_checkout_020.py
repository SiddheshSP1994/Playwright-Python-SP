import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-1141", "title": "Checkout scenario 1141", "data": {"sku": "SKU1141", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1141@example.com", "threshold": 410}},
    {"id": "CHECKOUT-1142", "title": "Checkout scenario 1142", "data": {"sku": "SKU1142", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1142@example.com", "threshold": 420}},
    {"id": "CHECKOUT-1143", "title": "Checkout scenario 1143", "data": {"sku": "SKU1143", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1143@example.com", "threshold": 430}},
    {"id": "CHECKOUT-1144", "title": "Checkout scenario 1144", "data": {"sku": "SKU1144", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1144@example.com", "threshold": 440}},
    {"id": "CHECKOUT-1145", "title": "Checkout scenario 1145", "data": {"sku": "SKU1145", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1145@example.com", "threshold": 450}},
    {"id": "CHECKOUT-1146", "title": "Checkout scenario 1146", "data": {"sku": "SKU1146", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1146@example.com", "threshold": 460}},
    {"id": "CHECKOUT-1147", "title": "Checkout scenario 1147", "data": {"sku": "SKU1147", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1147@example.com", "threshold": 470}},
    {"id": "CHECKOUT-1148", "title": "Checkout scenario 1148", "data": {"sku": "SKU1148", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1148@example.com", "threshold": 480}},
    {"id": "CHECKOUT-1149", "title": "Checkout scenario 1149", "data": {"sku": "SKU1149", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1149@example.com", "threshold": 490}},
    {"id": "CHECKOUT-1150", "title": "Checkout scenario 1150", "data": {"sku": "SKU1150", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1150@example.com", "threshold": 500}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
