import React from 'react'
import { Route, Switch } from 'react-router-dom'
import PropTypes from 'prop-types'

import Footer from 'components/Footer'
import Auth from 'components/Auth'
import './styles.scss'

const App = (props) => [
  // nav

  // routes
  props.isLoggedIn ? <PrivateRoutes key={2} /> : <PublicRoutes key={2} />,
  // footer
  <Footer key={3} />
]

App.propTypes = {
  isLoggedIn: PropTypes.bool.isRequired
}

const PrivateRoutes = (props) => (
  <Switch>
    <Route exact path='/' render={() => "Feed"} />
    <Route exact path='/explore' render={() => "Explore"} />
  </Switch>
)

const PublicRoutes = (props) => (
  <Switch>
    <Route exact path='/' component={Auth} />
    <Route exact path='/forgot' render={() => "Password"} />
  </Switch>
)

export default App
