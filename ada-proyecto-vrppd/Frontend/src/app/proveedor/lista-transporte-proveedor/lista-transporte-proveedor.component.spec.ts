import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaTransporteProveedorComponent } from './lista-transporte-proveedor.component';

describe('ListaTransporteProveedorComponent', () => {
  let component: ListaTransporteProveedorComponent;
  let fixture: ComponentFixture<ListaTransporteProveedorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaTransporteProveedorComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ListaTransporteProveedorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
