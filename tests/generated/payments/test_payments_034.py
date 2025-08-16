import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2011", "title": "Payments scenario 2011", "data": {"sku": "SKU2011", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2011@example.com", "threshold": 110}},
    {"id": "PAYMENTS-2012", "title": "Payments scenario 2012", "data": {"sku": "SKU2012", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2012@example.com", "threshold": 120}},
    {"id": "PAYMENTS-2013", "title": "Payments scenario 2013", "data": {"sku": "SKU2013", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2013@example.com", "threshold": 130}},
    {"id": "PAYMENTS-2014", "title": "Payments scenario 2014", "data": {"sku": "SKU2014", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2014@example.com", "threshold": 140}},
    {"id": "PAYMENTS-2015", "title": "Payments scenario 2015", "data": {"sku": "SKU2015", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2015@example.com", "threshold": 150}},
    {"id": "PAYMENTS-2016", "title": "Payments scenario 2016", "data": {"sku": "SKU2016", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2016@example.com", "threshold": 160}},
    {"id": "PAYMENTS-2017", "title": "Payments scenario 2017", "data": {"sku": "SKU2017", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2017@example.com", "threshold": 170}},
    {"id": "PAYMENTS-2018", "title": "Payments scenario 2018", "data": {"sku": "SKU2018", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2018@example.com", "threshold": 180}},
    {"id": "PAYMENTS-2019", "title": "Payments scenario 2019", "data": {"sku": "SKU2019", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2019@example.com", "threshold": 190}},
    {"id": "PAYMENTS-2020", "title": "Payments scenario 2020", "data": {"sku": "SKU2020", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2020@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
