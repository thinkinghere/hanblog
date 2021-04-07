from sanic_wtf import SanicForm as _SanicForm, FileAllowed, FileRequired
import markupsafe
from wtforms import (
    PasswordField, StringField, SubmitField, BooleanField, IntegerField,
    SelectField, SelectMultipleField, TextAreaField, FileField)
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired


class SanicForm(_SanicForm):

    def hidden_tag(self, *fields):
        def hidden_fields(fields):
            for f in fields:
                if isinstance(f, str):
                    f = getattr(self, f, None)

                if f is None or not isinstance(f.widget, HiddenInput):
                    continue

                yield f

        return markupsafe.Markup(
            u'\n'.join(str(f) for f in hidden_fields(fields or self))
        )

    def validate(self, extra_validators=None):
        self._errors = None
        success = True
        for name, field in self._fields.items():
            if field.type in ('SelectField', 'SelectMultipleField'):
                continue
            if extra_validators is not None and name in extra_validators:
                extra = extra_validators[name]
            else:
                extra = tuple()
            if not field.validate(self, extra):
                success = False
        return success


class LoginForm(SanicForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
