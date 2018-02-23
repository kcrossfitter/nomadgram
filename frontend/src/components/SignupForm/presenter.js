import React from 'react'
import Ionicon from 'react-ionicons'
import PropTypes from 'prop-types'

import formStyles from 'shared/formStyles.scss'

const SignupForm = (props, context) => (
  <div className={formStyles.formComponent}>
    <h3>
      {context.t('Signup to see photos and videos from your friends.')}
    </h3>
    <button className={formStyles.button}>
      {" "}
      <Ionicon icon="logo-facebook" fontSize="20px" color="#ffffff" />
      {context.t('Login with Facebook')}
    </button>
    <span className={formStyles.divider}>or</span>
    <form className={formStyles.form} onSubmit={props.handleSubmit}>
      <input
        type="email"
        placeholder={context.t('Email')}
        className={formStyles.textInput}
        value={props.emailValue}
        onChange={props.handleInputChange}
        name="email"
      />
      <input
        type="text"
        placeholder={context.t('Full Name')}
        className={formStyles.textInput}
        value={props.fullNameValue}
        onChange={props.handleInputChange}
        name="fullName"
      />
      <input
        type="username"
        placeholder={context.t('Username')}
        className={formStyles.textInput}
        value={props.usernameValue}
        onChange={props.handleInputChange}
        name="username"
      />
      <input
        type="password"
        placeholder={context.t('Password')}
        className={formStyles.textInput}
        value={props.passwordValue}
        onChange={props.handleInputChange}
        name="password"
      />
      <input
        type="submit"
        value={context.t('Sign up')}
        className={formStyles.button}
      />
    </form>
    <p className={formStyles.terms}>
      {context.t('By signing up, you agree to our')}
      <span>
        {context.t('terms & Privacy Policy')}
      </span>
    </p>
  </div>
)

SignupForm.propTypes = {
  emailValue: PropTypes.string.isRequired,
  fullNameValue: PropTypes.string.isRequired,
  usernameValue: PropTypes.string.isRequired,
  passwordValue: PropTypes.string.isRequired,
  handleInputChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired
}

SignupForm.contextTypes = {
  t: PropTypes.func.isRequired
}

export default SignupForm
