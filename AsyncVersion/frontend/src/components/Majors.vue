<template>
	<div class="majors">
		<table class="table">
			<thead class="thead-inverse">
				<tr>
					<th>Carrera</th>
					<th>Numero de publicaciones</th>
					<th>Temas</th>
					<th>Última publicación</th>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(major, index) in majors" :key="index">
					<td>
						<a>{{ major.name }}</a>
						<small class="text-muted d-block">{{ major.description }}</small>
					</td>
					<td class="align-middle">0</td>
					<td class="align-middle">0</td>
					<td></td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	name: 'Stats',

	data() {
		return {
			majors: [],
			errors: []
		}
	},

	methods: {
		getMajors() {

			axios.get('http://127.0.0.1:8000/majors/')
					.then(response => {
						this.majors = response.data
					})
					.catch(e => {
						this.errors.push(e)
					})
			}
	},

	created() {
		this.getMajors()
	}
}
</script>


