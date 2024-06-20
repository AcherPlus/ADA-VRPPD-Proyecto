import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditarListaTransporteProveedorComponent } from './editar-lista-transporte-proveedor.component';

describe('EditarListaTransporteProveedorComponent', () => {
  let component: EditarListaTransporteProveedorComponent;
  let fixture: ComponentFixture<EditarListaTransporteProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EditarListaTransporteProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EditarListaTransporteProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
