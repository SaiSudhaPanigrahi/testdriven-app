import React from 'react'
import axios from 'axios'
import { Route, Switch } from 'react-router-dom'

import UsersList from './components/UsersList'
import AddUser from './components/AddUser'
import About from './components/About'
import NavBar from './components/NavBar'
import Form from './components/Form'

class App extends React.Component {
  constructor() {
    super()
    this.state = {
      users: [],
      username: '',
      email: '',
      title: 'Testdriven App',
      formData: {
        username: '',
        email: '',
        password: '',
      },
      isAuthenticated: false,
    }
  }

  componentDidMount = () => {
    this.getUsers()
  }

  getUsers = () => {
    axios
      .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
      .then(res => this.setState({ users: res.data.data.users }))
      .catch(err => console.error(err))
  }

  addUser = event => {
    event.preventDefault()
    const data = {
      username: this.state.username,
      email: this.state.email,
    }
    axios
      .post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
      .then(() => {
        this.getUsers()
        this.setState({ username: '', email: '' })
      })
      .catch(err => console.log(err))
  }

  handleChange = event => {
    const obj = {}
    obj[event.target.name] = event.target.value
    this.setState(obj)
  }

  handleFormChange = event => {
    const obj = this.state.formData
    obj[event.target.name] = event.target.value
    this.setState(obj)
  }

  handleUserFormSubmit = event => {
    event.preventDefault()
    const formType = window.location.href.split('/').reverse()[0]
    let data = {
      email: this.state.formData.email,
      password: this.state.formData.password,
    }
    if (formType === 'register') {
      data.username = this.state.formData.username
    }
    const url = `${process.env.REACT_APP_USERS_SERVICE_URL}/auth/${formType}`
    axios
      .post(url, data)
      .then(res => {
        this.clearFormState()
        window.localStorage.setItem('authToken', res.data.auth_token)
        this.setState({ isAuthenticated: true })
        this.getUsers()
      })
      .catch(err => console.error(err))
  }

  clearFormState = () => {
    this.setState({
      formData: { username: '', email: '', password: '' },
      username: '',
      email: '',
    })
  }

  render() {
    const {
      users,
      username,
      email,
      title,
      formData,
      isAuthenticated,
    } = this.state

    return (
      <>
        <NavBar title={title} />
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
                        <h1 className="title is-1">All Users</h1>
                        <hr />
                        <br />
                        <AddUser
                          addUser={this.addUser}
                          username={username}
                          email={email}
                          handleChange={this.handleChange}
                        />
                        <br />
                        <hr />
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
                        formData={formData}
                        handleFormChange={this.handleFormChange}
                        handleUserFormSubmit={this.handleUserFormSubmit}
                        isAuthenticated={isAuthenticated}
                      />
                    )}
                  />
                  <Route
                    exact
                    path="/login"
                    render={() => (
                      <Form
                        formType={'Login'}
                        formData={formData}
                        handleFormChange={this.handleFormChange}
                        handleUserFormSubmit={this.handleUserFormSubmit}
                        isAuthenticated={isAuthenticated}
                      />
                    )}
                  />
                  )}
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