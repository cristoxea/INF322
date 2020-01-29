/**
@license
Copyright (c) 2018 The Polymer Project Authors. All rights reserved.
This code may only be used under the BSD style license found at http://polymer.github.io/LICENSE.txt
The complete set of authors may be found at http://polymer.github.io/AUTHORS.txt
The complete set of contributors may be found at http://polymer.github.io/CONTRIBUTORS.txt
Code distributed by Google as part of the polymer project is also
subject to an additional IP rights grant found at http://polymer.github.io/PATENTS.txt
*/

import {LitElement, html, css, property, customElement} from 'lit-element';
import { connect } from 'pwa-helpers/connect-mixin.js';
import { store } from '../store';
import { ButtonSharedStyles } from './button-shared-styles';
import { ListaCursos } from '../reducers/cursos';
import 'fontawesome-icon';


@customElement('horario-clases')
export class HorarioClases extends connect(store)(LitElement) {
  @property({type: Object})
  public cursos: ListaCursos = {};

  static get styles() {
    return [ButtonSharedStyles,
      css`
        :host {
            display: block;
        }
        
        .Sigla {
            width: 10% 
        }
        
        .Asignatura{
            width: 25%
        }
        
        .departamento{
            width: 13%
        }
        
        .paralelo{
            width: 22%
        }
        
        .profesor{
            width: 15%
        }
        
        .cupos{
            width: 5%
        }
        
        .horario{
            width: 10%
        }
        
        .left{
            text-align: left;
        }
      `
    ];
  }

  handleClick(e : any) {
    var button = e.target;
    if(button.prefix == "far"){
      button.setAttribute("prefix","fas");
      console.log(e.target.id);
    }else{
      button.setAttribute("prefix","far");
    }
  }

  protected render() {
    return html`
<!--<script type="module" src="../../node_modules/list.js">
</script>
<script>
new List('asignaturas',
        {
          valueNames:['asignatura', 'sigla'],
          page: 15,
          pagination: true
        });
</script>-->
<div class="asignaturas">
<strong>Buscar:</strong> <input type="text" class="search" />
<h2>Listado de Cursos</h2>
    <table style="box-sizing: content-box">
      <tbody>
      <div class="list">
      <tr>
          <th class="Sigla" style="text-align: left">
            <strong> Sigla </strong>
          </th>
          <th class="Asignatura" style="text-align: left">
            <strong> Asignatura </strong>
          </th>
          <th class="cupos" style="text-align: left">
          <strong> Más información </strong>
          </th>
        </tr>
      ${Object.keys(this.cursos).map((key) => {
      const item = this.cursos[key];
      return html`
        ${Object.keys(item.paralelos).map((idies) => {
        if(idies == '0'){
          return html`
          <tr>
          <td class="sigla" style="width: 9%; text-align: center; background-color: #f5f3ed">
            ${item.sigla}
          </td>
          <td class="asignatura" style="width: 9%;  background-color: #f5f3ed">
            ${item.asignatura}
          </td>
          <td style="width: 9%; text-align: center; background-color: #f5f3ed">
          <button @click="${this.handleClick}">
            <fontawesome-icon id="${item.sigla}" prefix="far" name="plus-square" fixed-width></fontawesome-icon>
          </button>
          </td> 
        </tr>
          `;
        } else {
          return html`
          `;
        }
      })}
        `;
    })}
      </tbody>
      </table> 
      </div>
          <ul class="pagination"></ul>
</div>
    `;
  
  }
}
