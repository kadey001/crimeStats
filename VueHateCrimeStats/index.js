var app = new Vue({
	el: '#app',
	data: {
		cityName: 'Los Angeles',
		city: {},
		cities: [],
		stateName: 'California',
		allStatesTotals: [],
		stateData: [],
		minority: '',
		bestMinorityStates: [],
		rankedStates: [],
	},
	created() {
		this.getCityData(this.cityName);
		this.getStateData(this.stateName);
		this.getCitiesData();
		this.getAllStates();
	},
	methods: {
		totalCrimes() {
			let city = this.city;
			return city.disability + city.gender + city.genderIdentity + city.race + city.sexOrientation;
		},
		rankStatesForMinority(minority) {
			rankedStates = [];
			//console.log(current);
			console.log(this.cityName);
			for (current in this.allStatesTotals) {
				if(current[minority]() == 0) {
					this.rankedStates.push(current.state);
				}
			}
		},
		getCityData(cityName) {
			const path = `http://127.0.0.1:5000/cities/${cityName}`;
			axios.get(path)
				.then((response) => {
					this.city = response.data[0];
				})
				.catch((error) => {
					console.log('An error occured. ' + error);
				})
		},
		getCitiesData() {
			const path = 'http://127.0.0.1:5000/cities';
			axios.get(path)
				.then((response) => {
					this.cities = response.data.sort((x, y) => ((x.agencyName == y.agencyName) ? 0 : ((x.agencyName > y.agencyName) ? 1 : -1)));
				})
				.catch((error) => {
					console.log('An error occured. ' + error);
				})
		},
		getAllStates() {
			const path = `http://127.0.0.1:5000/allStatesTotals`;
			axios.get(path)
				.then((response) => {
					this.allStatesTotals = response.data;
				})
				.catch((error) => {
					console.log('An error occured. ' + error);
				})
		},
		getStateData(stateName) {
			const path = `http://127.0.0.1:5000/state/${stateName}`;
			axios.get(path)
				.then((response) => {
					this.stateData = response.data;
				})
				.catch((error) => {
					console.log('An error occured. ' + error);
				})
		},
		getSafestStates(minority) {
			const path = `http://127.0.0.1:5000/safeStatesTotals/${minority}`;
			axios.get(path)
				.then((response) => {
					this.bestMinorityStates = response.data;
				})
				.catch((error) => {
					console.log('An error occured. ' + error);
				})
		}
	}
})