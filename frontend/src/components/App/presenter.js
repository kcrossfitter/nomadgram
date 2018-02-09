import React from 'react'
import { Route, Switch } from 'react-router-dom'

import Footer from 'components/Footer'
// import styles from './styles.scss'

const App = (props) => [
  // nav

  // routes
  props.isLoggedIn ? <PrivateRoutes key={2} /> : <PublicRoutes key={2} />,
  // footer
  <Footer key={3} />
]

const PrivateRoutes = (props) => (
  <Switch>
    <Route exact path='/' render={() => "Feed"} />
    <Route exact path='/explore' render={() => "Explore"} />
  </Switch>
)

const PublicRoutes = (props) => (
  <Switch>
    <Route exact path='/' render={() => "Login"} />
    <Route exact path='/forgot' render={() => "Password"} />
  </Switch>
)

// class App extends Component {
//   render() {
//     return (
//       <div className={styles.App}>
//         <Switch>
//           <Route exact path='/' component={() => 'hello'} />
//           <Route path='/login' component={() => 'login'} />
//         </Switch>
//         <Footer />
//       </div>
//     );
//   }
// }

export default App
