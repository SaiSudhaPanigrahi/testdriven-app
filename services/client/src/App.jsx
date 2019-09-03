import React from 'react'
import axios from 'axios'
import { Route, Switch } from 'react-router-dom'

import UsersList from './components/UsersList'
import About from './components/About'
import NavBar from './components/NavBar'
import Form from './components/forms/Form'
import Logout from './components/Logout'
import UserStatus from './components/UserStatus'
import Message from './components/Message'

class App extends React.Component {
  constructor() {
    super()
    this.state = {
      users: [],
      username: '',
      email: '',
      title: 'Testdriven App',
      isAuthenticated: false,
      messageName: null,
      messageType: null,
    }
    this.logoutUser = this.logoutUser.bind(this)
    this.loginUser = this.loginUser.bind(this)
    this.createMessage = this.createMessage.bind(this)
  }

  componentDidMount() {
    this.getUsers()
  }

  componentWillMount() {
    if (window.localStorage.getItem('authToken')) {
      this.setState({ isAuthenticated: true })
    }
  }

  getUsers() {
    axios
      .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
      .then(res => this.setState({ users: res.data.data.users }))
      .catch(err => console.error(err))
  }

  loginUser(token) {
    window.localStorage.setItem('authToken', token)
    this.setState({ isAuthenticated: true })
    this.getUsers()
    this.createMessage('Welcome', 'success')
  }

  logoutUser() {
    window.localStorage.clear()
    this.setState({ isAuthenticated: false })
  }

  createMessage(name = 'Sanity check', type = 'success') {
    this.setState({
      messageName: name,
      messageType: type,
    })
  }

  render() {
    const { users, title, isAuthenticated } = this.state

    return (
      <>
        <NavBar title={title} isAuthenticated={isAuthenticated} />
        <section className="section">
          <div className="container">
            {this.state.messageName && this.state.messageType && (
              <Message
                messageName={this.state.messageName}
                messageType={this.state.messageType}
              />
            )}
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
                        isAuthenticated={isAuthenticated}
                        loginUser={this.loginUser}
                        createMessage={this.createMessage}
                      />
                    )}
                  />
                  <Route
                    exact
                    path="/login"
                    render={() => (
                      <Form
                        formType={'Login'}
                        isAuthenticated={isAuthenticated}
                        loginUser={this.loginUser}
                        createMessage={this.createMessage}
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
