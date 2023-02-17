from constants import DOWN_PAYMENT, ANNUAL_RATE
from flask_restx import Resource, Namespace
from models import SmartPhone

smartphones_ns = Namespace('smartphones')


@smartphones_ns.route('/')
class SmartPhonesView(Resource):
    def get(self):
        sms = SmartPhone.query.all()
        res = []
        for s in sms:
            sm_d = s.__dict__
            del sm_d['_sa_instance_state']
            down_payment = sm_d["price"] * DOWN_PAYMENT
            sm_d["down_payment"] = down_payment
            sm_d["monthly_fee"] = ((sm_d["price"] - down_payment) * (1 + ANNUAL_RATE)) / 12
            res.append(sm_d)
        return res, 200
        smartphones


@smartphones_ns.route('/<int:smid>/')
class SmartPhoneView(Resource):
    def get(self, smid):
        s = SmartPhone.query.get_or_404(smid)
        sm_d = s.__dict__
        del sm_d['_sa_instance_state']
        down_payment = sm_d["price"] * DOWN_PAYMENT
        sm_d["down_payment"] = down_payment
        sm_d["monthly_fee"] = ((sm_d["price"] - down_payment) * (1 + ANNUAL_RATE)) / 12
        return sm_d, 200
