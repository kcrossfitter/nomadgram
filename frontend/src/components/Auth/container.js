import React, { Component } from 'react'

import Auth from './presenter'

class Container extends Component {
  state = {
    action: "login"
  }

  _changeAction = () => {
    this.setState(prevState => {
      const { action } = prevState

      if (action === "login") {
        return {
          action: "signup"
        }
      } else if (action === "signup") {
        return {
          action: "login"
        }
      }
    })
  }

  render() {
    const { action } = this.state
    
    return (
      <Auth action={action} changeAction={this._changeAction} />
    )
  }
}

export default Container