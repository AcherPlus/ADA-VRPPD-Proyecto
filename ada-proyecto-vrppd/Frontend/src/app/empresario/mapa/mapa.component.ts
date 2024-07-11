import { Component, OnInit } from '@angular/core';
import * as L from 'leaflet';

@Component({
  selector: 'app-mapa',
  standalone: true,
  imports: [],
  templateUrl: './mapa.component.html',
  styleUrl: './mapa.component.css'
})
export class MapaComponent implements OnInit {
  private map: any;
  private marker: any;

  constructor() { }

  ngOnInit(): void {
    this.initializeMap();
  }

  private initializeMap(): void {
    this.map = L.map('map').setView([-12.056, -77.043], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
    }).addTo(this.map);

    const customIcon = L.icon({
      iconUrl: 'assets/marker-icon.png',
      iconSize: [30, 40], // tamaño del icono
      iconAnchor: [22, 94], // punto del icono que corresponderá a la posición del marcador
      popupAnchor: [-3, -76] // punto desde el cual se abrirá el popup respecto al icono
    });
    
    
    this.marker = L.marker([-12.056, -77.043], {icon: customIcon, draggable: true}).addTo(this.map);

    this.map.on('click', (e: any) => {
      this.marker.setLatLng(e.latlng);
      this.updateLocationInfo(e.latlng);
    });

    this.marker.on('dragend', (e: any) => {
      this.updateLocationInfo(this.marker.getLatLng());
    });

    this.updateLocationInfo(this.marker.getLatLng());
  }

  private updateLocationInfo(latlng: any): void {
    fetch(`https://nominatim.openstreetmap.org/reverse?format=json&lat=${latlng.lat}&lon=${latlng.lng}`)
      .then(response => response.json())
      .then(data=> {
        const lat = Number(data.lat).toFixed(3);
        const lon = Number(data.lon).toFixed(3);

        document.getElementById('lat')!.innerText = `Latitud: ${lat}`;
        document.getElementById('lon')!.innerText = `Longitud: ${lon}`;
        document.getElementById('address')!.innerText = `Dirección: ${data.display_name}`;
        document.getElementById('district')!.innerText = `Distrito: ${data.address.district || data.address.neighbourhood || 'N/A'}`;
        document.getElementById('region')!.innerText = `Región: ${data.address.state || 'N/A'}`;
      })
      .catch(error => console.error("Error fetching geocoding data: ",error));
  }
}
