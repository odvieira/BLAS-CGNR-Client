import React from 'react'
import PostForm from '../components/PostForm'

function Application () {
	return (
		<div className="Application">
			<PostForm url='localhost:8000'/>			
		</div>
	)
}

export default Application