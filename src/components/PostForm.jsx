import React, {useState} from 'react'
import Axios from 'axios'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'

function PostForm(props) {
	const url = props.url
	const [Dataset, setDataset] = useState({
		Username:'',
		File:null,
		FileData:null
	})

	function handle(e) {
		const newData = {...Dataset}

		newData[e.target.id] = e.target.value
		setDataset(newData)
		console.log(newData)
	}

	function submit (e) {
		e.preventDefault()

		Axios.post(url + '/' + Dataset.Username, {
			File:Dataset.File.split('\\')[-1],
			FileData: Dataset.FileData
		})
	}

	function fileLoad(e) {
		e.preventDefault()

		const newData = {...Dataset}
		var file = e.target.files[0];
		var reader = new FileReader();

		newData[e.target.id] = e.target.value

		reader.onload = function(e) {
			// The file's text will be printed here
			console.log(e.target.result)
			newData.FileData=e.target.result.toString().replace(/\r/g,'').split('\n')
			setDataset(newData)

			console.log(newData)
		};

		reader.readAsText(file);
	}

	return (
		<div>
			<Form id="main-form" onSubmit={ (e) => submit(e) }>

			<Form.Group>
				<Form.Label>Username</Form.Label>
				<Form.Control
					type='text'
					id='Username'
					value={Dataset.Username}
					onChange=
						{ (e) => handle(e) }/>
			</Form.Group>

			<Form.Group>
				<Form.Label>File</Form.Label>
				<Form.Control
					type='file'
					id='File'
					value={Dataset.File}
					onChange=
					{ (e) => fileLoad(e) }
				/>
			</Form.Group>
			<Button variant="primary" type="submit" onClick={console.log('Submit')}>Submit</Button>
		</Form>		
		</div>
	)
}

export default PostForm
