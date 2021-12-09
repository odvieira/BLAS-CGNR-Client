import React from "react";
import "../scss/Header.scss"
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Container from 'react-bootstrap/Container'

class Header extends React.Component {
	render(){
		return (
			<div className="Header">
				 <Navbar bg="dark" variant="dark">
					<Container>
					<Nav className="me-auto">
						{this.props.pages.map( (x) =>
							<Nav.Link key={x.name.toString()} href={x.link}>
								{x.name}
							</Nav.Link>
						)}
					</Nav>
					</Container>
				</Navbar>		
			</div>
		)
	}
}

export default Header;