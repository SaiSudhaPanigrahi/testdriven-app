import React from 'react'

const AddUser = ({ addUser, username, email, handleChange }) => {
  return (
    <form action='' method='post' onSubmit={event => addUser(event)}>
      <div className='field'>
        <input
          className='input is-large'
          type='text'
          name='username'
          value={username}
          placeholder='Enter a username'
          onChange={handleChange}
          required
        />
      </div>
      <div className='field'>
        <input
          className='input is-large'
          type='email'
          name='email'
          value={email}
          onChange={handleChange}
          placeholder='Enter an email address'
          required
        />
      </div>
      <input
        type='submit'
        className='button is-primary is-large is-fullwidth'
        value='Submit'
      />
    </form>
  )
}

export default AddUser
