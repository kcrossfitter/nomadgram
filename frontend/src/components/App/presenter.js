import React from 'react'
import { Route, Switch } from 'react-router-dom'
import PropTypes from 'prop-types'

import Navigation from 'components/Navigation'
import Footer from 'components/Footer'
import Auth from 'components/Auth'
import Feed from 'components/Feed'
import './styles.scss'

const App = (props) => [
  // nav
  props.isLoggedIn ? <Navigation key={1} /> : null,
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
    <Route exact path='/' component={Feed} />
    <Route path='/explore' render={() => "Explore"} />
  </Switch>
)

const PublicRoutes = (props) => (
  <Switch>
    <Route exact path='/' component={Auth} />
    <Route path='/forgot' render={() => "Password"} />
  </Switch>
)

export default App
