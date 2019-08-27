import React from 'react'
import axios from 'axios'
import { Route, Switch } from 'react-router-dom'

import UsersList from './components/UsersList'
import About from './components/About'
import NavBar from './components/NavBar'
import Form from './components/forms/Form'
import Logout from './components/Logout'
import UserStatus from './components/UserStatus'

class App extends React.Component {
  constructor() {
    super()
    let authStatus = this.handleCheckTokenExists()
    this.state = {
      users: [],
      username: '',
      email: '',
      title: 'Testdriven App',
      isAuthenticated: authStatus,
    }
  }

  componentDidMount = () => {
    this.getUsers()
  }

  handleCheckTokenExists = () => {
    return window.localStorage.getItem('authToken') !== null
  }

  getUsers = () => {
    axios
      .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
      .then(res => this.setState({ users: res.data.data.users }))
      .catch(err => console.error(err))
  }

  loginUser = token => {
    window.localStorage.setItem('authToken', token)
    this.setState({ isAuthenticated: true })
    this.getUsers()
  }

  logoutUser = () => {
    window.localStorage.clear()
    this.setState({ isAuthenticated: false })
  }

  render() {
    const { users, title, isAuthenticated } = this.state

    return (
      <>
        <NavBar title={title} isAuthenticated={isAuthenticated} />
        <section className="section">
          <div className="container">
            <div className="columns">
              <div className="column is-half">
                <br />
                <Switch>
                  <Route
                    exact
                    path="/"
                    render={() => (
                      <div>
                        <UsersList users={users} />
                      </div>
                    )}
                  />
                  <Route exact path="/about" component={About} />
                  <Route
                    exact
                    path="/register"
                    render={() => (
                      <Form
                        formType={'Register'}
                        // use as `key` to reset Form
                        key={isAuthenticated}
                        isAuthenticated={isAuthenticated}
                        loginUser={this.loginUser}
                      />
                    )}
                  />
                  <Route
                    exact
                    path="/login"
                    render={() => (
                      <Form
                        formType={'Login'}
                        // use as `key` to reset Form
                        key={isAuthenticated}
                        isAuthenticated={isAuthenticated}
                        loginUser={this.loginUser}
                      />
                    )}
                  />
                  <Route
                    exact
                    path="/logout"
                    render={() => (
                      <Logout
                        logoutUser={this.logoutUser}
                        isAuthenticated={isAuthenticated}
                      />
                    )}
                  />
                  <Route
                    exact
                    path="/status"
                    render={() => (
                      <UserStatus isAuthenticated={isAuthenticated} />
                    )}
                  />
                </Switch>
              </div>
            </div>
          </div>
        </section>
      </>
    )
  }
}

export default App
