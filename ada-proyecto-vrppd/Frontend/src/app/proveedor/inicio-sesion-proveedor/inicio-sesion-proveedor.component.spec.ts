import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InicioSesionProveedorComponent } from './inicio-sesion-proveedor.component';

describe('InicioSesionProveedorComponent', () => {
  let component: InicioSesionProveedorComponent;
  let fixture: ComponentFixture<InicioSesionProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [InicioSesionProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(InicioSesionProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
