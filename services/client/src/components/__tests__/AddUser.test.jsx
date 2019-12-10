import React from 'react'
import { shallow } from 'enzyme'
import toJson from 'enzyme-to-json'

import AddUser from '../AddUser'

test('AddUser renders properly', () => {
  const wrapper = shallow(<AddUser />)
  const element = wrapper.find('form')
  expect(element.find('input').length).toBe(3)
  expect(element.find('input').get(0).props.name).toBe('username')
  expect(element.find('input').get(1).props.name).toBe('email')
  expect(element.find('input').get(2).props.type).toBe('submit')
})

test('Adduser renders a snapshot properly', () => {
  const tree = shallow(<AddUser />)
  expect(toJson(tree)).toMatchSnapshot()
})
