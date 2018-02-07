import { createStore, combineReducers } from 'redux'
import users from './modules/users'

const reducer = combineReducers({
  users: users
})

let store = initialState => createStore(reducer)

export default store()

