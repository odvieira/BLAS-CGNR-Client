import React, {useState} from 'react'
import Axios from 'axios'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import '../scss/PostForm.scss'


function PostForm(props) {
	const url = props.url
	const [File, setFile] = useState(null)
	const [FileData, setFileData] = useState(null)
	const [Dataset, setDataset] = useState({
		Username:'',
		Sensors: 64,
		Samples: 794
	})

	function handle(e) {
		const newData = {...Dataset}

		newData[e.target.id] = e.target.value
		setDataset(newData)
		console.log(newData)
	}

	function submit (e) {
		e.preventDefault()

		Axios.post(url + '/usuario', {
			File:File,
			FileData: FileData
		})
	}

	function fileLoad(e) {
		e.preventDefault()

		const newData = {...Dataset}
		var file = e.target.files[0];
		var reader = new FileReader();

		File = e.target.value

		reader.onload = function(e) {
			// The file's text will be printed here
			console.log(e.target.result)
			
			newData.FileData=e.target.result.toString()
													.replace(/\r/g,'')
													.split('\n')
													.map(x => Number(x).toFixed(8))
													
			// for(i=0; i<)

			setDataset(newData)

			console.log(newData)
		};

		reader.readAsText(file);
	}

	return (
		<div className="PostForm">
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
				<Form.Label>Número de sensores</Form.Label>
				<Form.Control
					type='number'
					id='Sensors'
					value={Dataset.Sensors}
					onChange=
						{ (e) => handle(e) }/>
			</Form.Group>

			<Form.Group>
				<Form.Label>Número de amostras</Form.Label>
				<Form.Control
					type='number'
					id='Samples'
					value={Dataset.Samples}
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
