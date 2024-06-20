import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AsignarTransporteComponent } from './asignar-transporte.component';

describe('AsignarTransporteComponent', () => {
  let component: AsignarTransporteComponent;
  let fixture: ComponentFixture<AsignarTransporteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AsignarTransporteComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AsignarTransporteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
