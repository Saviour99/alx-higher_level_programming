#!/usr/bin/node

const requests = require('request');
const fs = require('fs');

const getTheContent = (url, filePath) => {
	requests.get(url, (error, response, body) => {
		if (error){
			console.error(error);
		}
		else {
			const filePath = JSON.parse(body);

		}
	})
}
