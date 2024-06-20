import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearCuentaProveedorComponent } from './crear-cuenta-proveedor.component';

describe('CrearCuentaProveedorComponent', () => {
  let component: CrearCuentaProveedorComponent;
  let fixture: ComponentFixture<CrearCuentaProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CrearCuentaProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CrearCuentaProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
