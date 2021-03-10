"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField, DateField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

class IncomeForm(FlaskForm):
   """ Income Form """
   z_count = StringField("Z της Ημέρας", [DataRequired()])
   early_income = StringField("Πρωϊνός Τζίρος", [DataRequired()])
   late_income = StringField("Βραδυνός Τζίρος")
   notes = TextAreaField("Παρατηρήσεις", [Length(min=4, message=("Start a Note!"))] )
   submit = SubmitField("Αποστολή")
   
class OutcomeForm(FlaskForm):
   """ Outcome Form """
   date = DateField("Ημερομηνία")
   description = TextAreaField("Περιγραφή")
   invoice_num = StringField("Αρ. Τιμολογίου")
   total_cost = StringField("Συνολικό Κόστος")
   extra_cost = StringField("Επιπλέον Κοστολόγιο")
   tax_percent = StringField("ΦΠΑ Ποσοστό")
   tax_percent2 = StringField("Επιπλέον ΦΠΑ Ποσοστό")
   supplier = StringField("Προμηθευτής")
   staff_id = StringField("Εργαζόμενος")
   is_fix_cost = BooleanField("Πάγια έξοδα")
   is_purchase_cost = BooleanField("Έξοδα αγορών")
   is_salary_cost = BooleanField("Έξοδα Προσωπικού")
   is_insurance_cost = BooleanField("Έξοδα Ασφάλειας/ΙΚΑ")
   is_misc_cost = BooleanField("Διάφορα Έξοδα")
   paymeny_way = StringField("Τρόπος Πήρωμής")
   is_paid = StringField("Είναι πληρωμένο;")
   notes = TextAreaField("Παρατηρήσεις", [Length(min=4, message=("Start a Note!"))] )
   

