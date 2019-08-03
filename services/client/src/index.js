import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

import UsersList from './components/UsersList'
import AddUser from './components/AddUser'

class App extends React.Component {
  constructor () {
    super()
    this.state = {
      users: [],
      username: '',
      email: ''
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
      email: this.state.email
    }
    axios
      .post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
      .then(res => {
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

  render () {
    const { users, username, email } = this.state
    return (
      <section className='section'>
        <div className='container'>
          <div className='columns'>
            <div className='column is-half'>
              <br />
              <h1 className='title is-1'>All Users</h1>
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
          </div>
        </div>
      </section>
    )
  }
}
ReactDOM.render(<App />, document.getElementById('root'))
