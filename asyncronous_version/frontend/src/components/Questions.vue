<template>
  <div class="hello">
		<h1 class="display-3 text-center pt-5 pb-5 major-title">Questions</h1>
		<div class="card mb-3" v-for="(question, index) in questions" :key="index">
			<div class="card-body">
				<h5 class="card-title">{{ question.title }}</h5>
				<h6 class="card-subtitle mb-2 text-muted">{{ question.user_name}}</h6>
				<p class="card-text">{{ question.description }}</p>
			</div>
			<ul class="list-group list-group-flush">
				<li class="list-group-item">
					<ul class="list-unstyled">
						<a href="#">#Industrial</a>
						<a href="#">#Termodinamica</a>
						<a href="#">#MecanicaDeFluidos</a>
					</ul>
				</li>
			</ul>
			<div class="card-body">
				<div class="float-left">
					<a href="#" class="card-link">Responder pregunta</a>
					<a href="#" class="card-link">Me gusta</a>
					<a href="#" class="card-link">No me gusta</a>
					<a href="#" class="card-link">Reportar</a>
				</div>
				<div class="float-right">
					<span class="card-text"><strong>0</strong> respuestas</span>
					<span class="card-text"><strong>{{ question.current_score }}</strong> valoración</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Index',

	data() {
		return {
			questions: [],
			errors: []
		}
	},

	methods: {
		getQuestions() {

			axios.get('http://127.0.0.1:8000/questions/')
					.then(response => {
						this.questions = response.data
					})
					.catch(e => {
						this.errors.push(e)
					})

		}
	},

	created() {
		this.getQuestions()	
	}
}
</script>

<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
