import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0681", "title": "Orders scenario 681", "data": {"sku": "SKU681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user681@example.com", "threshold": 810}},
    {"id": "ORDERS-0682", "title": "Orders scenario 682", "data": {"sku": "SKU682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user682@example.com", "threshold": 820}},
    {"id": "ORDERS-0683", "title": "Orders scenario 683", "data": {"sku": "SKU683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user683@example.com", "threshold": 830}},
    {"id": "ORDERS-0684", "title": "Orders scenario 684", "data": {"sku": "SKU684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user684@example.com", "threshold": 840}},
    {"id": "ORDERS-0685", "title": "Orders scenario 685", "data": {"sku": "SKU685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user685@example.com", "threshold": 850}},
    {"id": "ORDERS-0686", "title": "Orders scenario 686", "data": {"sku": "SKU686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user686@example.com", "threshold": 860}},
    {"id": "ORDERS-0687", "title": "Orders scenario 687", "data": {"sku": "SKU687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user687@example.com", "threshold": 870}},
    {"id": "ORDERS-0688", "title": "Orders scenario 688", "data": {"sku": "SKU688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user688@example.com", "threshold": 880}},
    {"id": "ORDERS-0689", "title": "Orders scenario 689", "data": {"sku": "SKU689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user689@example.com", "threshold": 890}},
    {"id": "ORDERS-0690", "title": "Orders scenario 690", "data": {"sku": "SKU690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user690@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
