#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        kilometros = self.request.get("kilometros")
        tiempo = self.request.get("tiempo")
        consumo_medio = self.request.get("consumoMedio")

        if kilometros.isdigit() and tiempo.isdigit() and consumo_medio.isdigit():
            velocidad_media = float(kilometros) / float(tiempo)
            consumo_total = float(consumo_medio) * float(kilometros)

            self.response.write('Velocidad media: ' + str(velocidad_media) + ' km/s | Consumo total: ' + str(consumo_total) + ' L')
        else:
            self.response.write('Datos introducidos no validos')


app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
