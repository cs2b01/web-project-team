<template>
  <div id="app">
   <nav class="navbar navbar-expand-lg navbar-light bg-light">
			<a class="navbar-brand" href="#">Q&A UTEC</a>
			<button
				class="navbar-toggler"
				type="button"
				data-toggle="collapse"
				data-target="#navbarNav"
				aria-controls="navbarNav"
				aria-expanded="false"
				aria-label="Toggle navigation"
			>
				<span class="navbar-toggler-icon"></span>
			</button>
			<div class="collapse navbar-collapse" id="navbarNav">
				<ul class="navbar-nav">
					<li class="nav-item active">
						<a class="nav-link">
							<router-link to="/">Página principal</router-link>
						</a>
					</li>
					<li class="nav-item">
						<a class="nav-link">
							<router-link to="/majors">Carreras</router-link>
						</a>
					</li>
					<li class="nav-item">
						<a class="nav-link" href="#">Mi Perfil</a>
					</li>
				</ul>
			</div>
		</nav>
    <router-view/>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
