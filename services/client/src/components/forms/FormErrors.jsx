import React from 'react'

import './FormErrors.css'

const FormErrors = ({ formRules }) => {
  return (
    <div>
      <ul className="validation-list">
        {formRules.map(rule => {
          return (
            <li className={rule.valid ? 'success' : 'error'} key={rule.id}>
              {rule.name}
            </li>
          )
        })}
      </ul>
      <br />
    </div>
  )
}

export default FormErrors
