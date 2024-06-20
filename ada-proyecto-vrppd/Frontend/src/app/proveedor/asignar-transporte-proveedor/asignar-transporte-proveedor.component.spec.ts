import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AsignarTransporteProveedorComponent } from './asignar-transporte-proveedor.component';

describe('AsignarTransporteProveedorComponent', () => {
  let component: AsignarTransporteProveedorComponent;
  let fixture: ComponentFixture<AsignarTransporteProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AsignarTransporteProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AsignarTransporteProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
