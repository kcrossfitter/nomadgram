import React, { Component } from 'react'

import LoginForm from './presenter'

class Container extends Component {
  state = {
    username: '',
    password: ''
  }

  _handleInputChange = (event) => {
    const { target: { value, name } } = event
    this.setState({
      [name]: value
    })
    console.log(this.state)
  }

  _handleSubmit = (event) => {
    event.preventDefault()
    console.log(this.state)
    // redux action will be here
  }

  render() {
    const { username, password } = this.state
    return (
      <LoginForm
        usernameValue={username}
        passwordValue={password}
        handleInputChange={this._handleInputChange}
        handleSubmit={this._handleSubmit}
      />
    )
  }
}

export default Container
